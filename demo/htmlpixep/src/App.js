import logo from './logo.svg';
import './App.css';
import getPixels from 'get-pixels'
function App() {
  function sayHello() {
    alert('Hello!');
  }
  
  async function loginUser() {
    return fetch('http://localhost:8080/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((data) =>{ console.log(data.json())})
  }
  return (
    <div className="App">
      <header className="App-header">
        <p onClick={console.log("Hello")}>Hello</p>
        <img src={logo} className="App-logo" alt="logo" onClick={loginUser()}/>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer" o
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
