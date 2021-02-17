import React from 'react';
import ReactDom from 'react-dom';


const App = () => {
    return (
        <h1>Hello world from React</h1>
    )
}

ReactDom.render(<App />, document.getElementById('app'));
