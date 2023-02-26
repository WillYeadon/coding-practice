import logo from './logo.svg';
import './App.css';
import React from 'react';
import ReactPlayer from "react-player/youtube";

function Header() {
  return <h1>Hello World!</h1>
}

const App = () => {
  return (
    <div>
      <Header />
      <MyVideo />
    </div>
  );
};

const MyVideo = () => {
  return (
    <ReactPlayer url='https://www.youtube.com/watch?v=ysz5S6PUM-U' />
  );
};

export default App;
