import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from '../logos/logo.png'; // Ensure this path is correct

function RegisterPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const navigate = useNavigate();

  const handleRegister = (e) => {
    e.preventDefault();
    // Placeholder for backend registration logic
    navigate('/home');
  };

  const styles = {
    registerPage: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '20px',
      height: '545px',
      backgroundColor: '#F1FAEE', // Custom background color
      fontFamily: "'Dangrek', cursive", // Applying Dangrek font
    },
    logo: {
      maxWidth: '100px', // Mini version of the logo
      marginBottom: '20px', // Space between logo and form
    },
    formTitle: {
      fontSize: '1.5rem',
      color: '#173155', // Using the same palette
      marginBottom: '20px', // Space above the form fields
      fontFamily: "'Dangrek', cursive", // Applying Dangrek font
    },
    input: {
      margin: '10px 0',
      padding: '10px',
      borderRadius: '5px',
      border: '2px solid #A8DADC', // Light blue from the palette
      width: '300px',
      fontSize: '16px',
    },
    button: {
      flex: '1',
      margin: '20px 0',
      padding: '10px 0',
      backgroundColor: '#E63946', // Red background for buttons
      color: 'white',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
      textDecoration: 'none',
      textAlign: 'center',
      width: 'calc(300px + 20px)', // To match the input field width including padding
      fontFamily: "'Dangrek', cursive",

    },
  };

  return (
    <div style={styles.registerPage}>
      <img src={logo} alt="LumiPlan Logo" style={styles.logo} />
      <div style={styles.formTitle}>LumiPlan</div>
      <form onSubmit={handleRegister} style={{ width: '100%', maxWidth: '330px' }}>
        <input
          type="text"
          placeholder="Enter Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={styles.input}
          required
        />
        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={styles.input}
          required
        />
        <input
          type="password"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={styles.input}
          required
        />
        <button type="submit" style={styles.button}>Register</button>
      </form>
    </div>
  );
}

export default RegisterPage;
