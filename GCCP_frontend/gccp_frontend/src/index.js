import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import CreateEvent from './pages/CreateEvent';
import Members from './components/members';

import AddMember from './pages/AddMember';
import ViewMembers from './pages/ViewMembers';
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}>
          <Route index element={<App />} />
        </Route>
        <Route path="/CreateEvent" element={<CreateEvent/>} />
        <Route path="/members" element={<Members/>} />
        
         
        <Route path="/AddMember" element={<AddMember/>} />
        <Route path="/ViewMembers" element={<ViewMembers/>} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
