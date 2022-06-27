import React from 'react';
import logo from './logo.svg';
import './App.css';
import Navbar from './Components/Navbar';

import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import AudioRecog from './Container/AudioRecog';

const App = () => {
  return (
    <div className="flex flex-col w-9/12 mx-auto ">
      <Router>
      <Navbar />
        <Routes>
          <Route path='/audio' element={<AudioRecog />} />
        </Routes>
      </Router>
    </div>
  )
}
export default App;
