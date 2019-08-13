import React from 'react';
import './App.css';
import AccordionItems from './components/accordion/AccordionItems'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <AccordionItems />
      </header>
    </div>
  );
}

export default App;
