import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import AppStyle from './styles/App.css'


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
        <App className={AppStyle}/>
);

