import React from 'react';
import './About.css';

const About = () => {
  return (
    <div>
        <div className='about-container'>
        <h1>About Us</h1>
        <p>Learn more about us on this page.</p>
        </div>
        <div className='location-container'>
            <h2>Location</h2>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3018.1878436251714!2d-73.98788572411!3d40.84579947137373!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2f71d18b90e2f%3A0x41810759534e95a!2s460%20Bergen%20Blvd%20%23266%2C%20Palisades%20Park%2C%20NJ%2007650!5e0!3m2!1sen!2sus!4v1726136047214!5m2!1sen!2sus"             width="600"
                height='450'
                style = {{border: 0}}
                allowFullScreen = ""
                loading='lazy'
                title='location'
                ></iframe>
        </div>
        <div className='hours-container'>
            <h2>Busines Hours</h2>
            <ul>
            <li>Monday: 9:00 AM - 5:00 PM</li>
            <li>Tuesday: 9:00 AM - 5:00 PM</li>
            <li>Wednesday: 9:00 AM - 5:00 PM</li>
            <li>Thursday: 9:00 AM - 5:00 PM</li>
            <li>Friday: 9:00 AM - 5:00 PM</li>
            <li>Saturday: 10:00 AM - 4:00 PM</li>
            <li>Sunday: Closed</li>
            </ul>
        </div>
    </div>
  );
};

export default About;