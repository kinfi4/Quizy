import React from 'react';
import ReactDom from 'react-dom';
import { Provider } from 'react-redux';
import store from '../store'; 
import Quizzes from './quizzes/Quizzes';
import MainApp from './../components/app/MainApp';
import { BrowserRouter, Route } from 'react-router-dom';


const App = () => {
    return (
        <Provider store={store}>
            <BrowserRouter>
                    <div className="app-wrapper">
                        <Route exact path="/welcome" render={() => <Quizzes />} />
                        <Route path="/app" render={() => <MainApp />} />
                    </div>
            </BrowserRouter>
        </Provider>
    )
}

ReactDom.render(
        <App />
   , document.getElementById('app')
);
