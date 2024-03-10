import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../logos/logo.png'; // Ensure this path is correct

function LandingPage() {
  const styles = {
    landingPage: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '20px',
      backgroundColor: '#F1FAEE', // Custom background color
      color: '#1D3557', // Dark blue text color
      height: '545px' ,
      fontFamily: "'Dangrek', cursive", // Applying Dangrek font
    },
    logo: {
      maxWidth: '300px',
      height: 'auto',
      marginBottom: '20px', // Space between logo and title
    },
    title: {
      font: 'sans-serif' ,
      fontSize: '3.5rem',
      color: '#173155', // Blue color for the title
      marginBottom: '20px', // Space between title and buttons
    },
    buttonsContainer: {
      display: 'flex',
      justifyContent: 'center', // Center the buttons container
      width: '100%', // Take full width to center content
      maxWidth: '300px', // Max width to control button sizes
    },
    button: {
      flex: '1', // Make buttons take up equal space
      margin: '0 10px', // Space between buttons
      padding: '10px 0', // Padding to ensure buttons are the same size vertically
      backgroundColor: '#E63946', // Red background for buttons
      color: 'white',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
      textDecoration: 'none',
      textAlign: 'center', // Center text inside buttons
    },
  };

  return (
    <div style={styles.landingPage}>
      <img src={logo} alt="LumiPlan Logo" style={styles.logo} />
      <div style={styles.title}>LumiPlan</div>
      <div style={styles.buttonsContainer}>
        <Link to="/login" style={{ ...styles.button, margin: '0 10px 0 0' }}>Login</Link> {/* Adjusted margin for first button */}
        <Link to="/register" style={{ ...styles.button, margin: '0 0 0 10px' }}>Register</Link> {/* Adjusted margin for second button */}
      </div>
    </div>
  );
}

export default LandingPage;
