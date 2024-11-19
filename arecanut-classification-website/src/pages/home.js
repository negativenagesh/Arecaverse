import React from 'react';
import './Home.css';

const Home = () => {
    return (
        <div className="home-container">
            <h1>Welcome to Arecanut Classification</h1>
            <p>Identify and classify the quality of arecanuts using advanced machine learning models.</p>
            <img src="/arecanut.jpg" alt="Arecanut" className="arecanut-image" />
        </div>
    );
};

export default Home;