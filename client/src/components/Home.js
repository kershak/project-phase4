import React from "react";
//import SimpleImageSlider from "react-simple-image-slider";
import './Home.css';
import {Link} from 'react-router-dom'

function Home(){

  const sliderImages = [
    {
      url: "images/ATC-HZ5510C.png",
    },
    {
      url:"images/ATC-HZ5530T.png",
    },
    {
      url:"images/ATC-HZ7810C.png",
    },
    {
      url:"images/ATC-HZ7830T.png",
    },
  ];

  return (
      <main className='home'>
        <h1>Welcome to Ascent Imaging</h1>
        <p>Please Log in <Link to ="/returns">Here</Link></p>
        {/* <p>Your imaging solutions partner.</p> */}
        <div className="slider-container">
        {/* <SimpleImageSlider
            width={900}
            height={600}
            images={sliderImages}
            showNavs={true}
          />  */}
        </div>
      </main>
  );
};

export default Home;