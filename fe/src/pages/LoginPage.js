import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from '../logos/logo.png'; // Ensure this path is correct

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    navigate('/home');
  };

  const styles = {
    loginPage: {
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '20px',
      height: '100vh',
      backgroundColor: '#F1FAEE',
      fontFamily: "'Dangrek', cursive",
    },
    logo: {
      maxWidth: '100px', // Adjust for mini logo
      marginBottom: '10px', // Space between logo and "LumiPlan" text
    },
    title: {
      marginBottom: '10px', // Space between "LumiPlan" text and form
      color: '#173155', // Using the color you specified for the title
      fontSize: '1.5rem', // Adjusted for consistency
    },
    input: {
      margin: '10px 0',
      padding: '10px',
      borderRadius: '5px',
      border: '2px solid #A8DADC',
      width: '300px',
      fontSize: '16px',
    },
    button: {
      margin: '20px 0',
      padding: '10px 0',
      backgroundColor: '#E63946',
      color: 'white',
      border: 'none',
      borderRadius: '5px',
      width: 'calc(300px + 20px)',
      cursor: 'pointer',
      textDecoration: 'none',
      textAlign: 'center',
      fontSize: '16px',
      fontFamily: "'Dangrek', cursive", // Applying Dangrek font
    },
  };

  return (
    <div style={styles.loginPage}>
      <img src={logo} alt="LumiPlan Logo" style={styles.logo} />
      <div style={styles.title}>LumiPlan</div>
      <form onSubmit={handleLogin} style={{ width: '100%', maxWidth: '330px' }}>
        
        <input
          type="text"
          placeholder="Enter Username"
          
          value={username}
          onChange={(e) => setUsername(e.target.value)}
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
        <button type="submit" style={styles.button}>Login</button>
      </form>
    </div>
  );
}

export default LoginPage;
