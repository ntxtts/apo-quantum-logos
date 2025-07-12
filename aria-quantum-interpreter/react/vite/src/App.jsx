import React, { useState, useEffect } from 'react';
import Plotly from 'plotly.js-dist-min';
import * as d3 from 'd3';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    // Fetch Bloch Sphere Data
    fetch('http://localhost:7071/api/quantumState?state=+&operation=analyze')
      .then(res => res.json())
      .then(data => {
        const blochData = [{
          type: 'scatter3d',
          mode: 'markers',
          x: [data.x], y: [data.y], z: [data.z],
          marker: { size: 5, color: 'blue' }
        }];

        const blochLayout = {
          scene: {
            xaxis: { range: [-1, 1] },
            yaxis: { range: [-1, 1] },
            zaxis: { range: [-1, 1] },
          },
          title: 'Bloch Sphere'
        };

        Plotly.newPlot('blochSphere', blochData, blochLayout);
      });

    // Fetch Density Matrix Data
    fetch('http://localhost:7071/api/quantumState?operation=tomography')
      .then(res => res.json())
      .then(data => {
        Plotly.newPlot('densityMatrix', [{
          z: data.matrix,
          type: 'heatmap',
          colorscale: 'Viridis'
        }], { title: 'Density Matrix' });
      });

    // Fetch Symbolic Trace Data
    fetch('http://localhost:7071/api/reflector', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: 'symbolic trace' })
    })
      .then(res => res.json())
      .then(data => {
        d3.select('#symbolGraph').selectAll('*').remove();
        const svg = d3.select('#symbolGraph')
          .append('svg')
          .attr('width', 600)
          .attr('height', 400);

        const simulation = d3.forceSimulation(data.nodes)
          .force('link', d3.forceLink(data.links).id(d => d.id).distance(150))
          .force('charge', d3.forceManyBody())
          .force('center', d3.forceCenter(300, 200));

        const link = svg.selectAll('line')
          .data(data.links)
          .enter().append('line')
          .attr('stroke', 'gray');

        const node = svg.selectAll('circle')
          .data(data.nodes)
          .enter().append('circle')
          .attr('r', 10)
          .attr('fill', 'blue');

        const text = svg.selectAll('text')
          .data(data.nodes)
          .enter().append('text')
          .text(d => d.id)
          .attr('font-size', 15)
          .attr('dx', 12)
          .attr('dy', 4);

        simulation.on('tick', () => {
          node.attr('cx', d => d.x).attr('cy', d => d.y);
          text.attr('x', d => d.x).attr('y', d => d.y);
          link
            .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
        });
      });

    // Fetch Histogram Data
    const fetchHistogram = async () => {
      try {
        const res = await fetch('http://localhost:7071/api/quantumCircuit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ operation: 'histogram' })
        });
        const data = await res.json();
        Plotly.newPlot('histogram', [{
          x: data.x,
          y: data.y,
          type: 'bar',
          marker: { color: 'orange' }
        }], { title: 'Histogram' });
      } catch (error) {
        console.error('Error fetching histogram data:', error);
      }
    };

    // Fetch Circuit Diagram Data
    const fetchCircuitDiagram = async () => {
      try {
        const res = await fetch('http://localhost:7071/api/quantumCircuit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ operation: 'circuit' })
        });
        // Render circuit diagram (placeholder logic)
        d3.select('#circuitDiagram').selectAll('*').remove();
        const svg = d3.select('#circuitDiagram')
          .append('svg')
          .attr('width', 600)
          .attr('height', 400);

        svg.selectAll('rect')
          .data(data.gates)
          .enter().append('rect')
          .attr('x', (d, i) => i * 50)
          .attr('y', 50)
          .attr('width', 40)
          .attr('height', 40)
          .attr('fill', 'green');

        svg.selectAll('text')
          .data(data.gates)
          .enter().append('text')
          .attr('x', (d, i) => i * 50 + 20)
          .attr('y', 75)
          .attr('text-anchor', 'middle')
          .text(d => d.label);
      } catch (error) {
        console.error('Error fetching circuit diagram data:', error);
      }
    };

    fetchHistogram();
    fetchCircuitDiagram();
  }, []);

  const handleCommandSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:7071/api/runAria?command=' + encodeURIComponent(command));
      const data = await res.json();
      setResponse(JSON.stringify(data, null, 2));
    } catch (error) {
      setResponse('Error: ' + error.message);
    }
  };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Quantum Dashboard</h1>
      <form onSubmit={handleCommandSubmit}>
        <input
          type="text"
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          placeholder="Enter a quantum command"
        />
        <button type="submit">Run Command</button>
      </form>
      <h2>Response:</h2>
      <pre>{response}</pre>
      <div className="visualizations">
        <h2>Visualizations</h2>
        <div id="blochSphere" style={{ height: '400px' }}></div>
        <div id="densityMatrix" style={{ height: '400px' }}></div>
        <div id="symbolGraph"></div>
        <div id="histogram" style={{ height: '400px' }}></div>
        <div id="circuitDiagram" style={{ height: '400px' }}></div>
      </div>
    </>
  );
}

export default App;
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      external: ['plotly.js-dist-min']
    }
  }
});
