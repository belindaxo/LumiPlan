import React from 'react';

function HomePage() {
  const styles = {
    homePage: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      fontFamily: "'Dangrek', cursive",
      backgroundColor: '#F1FAEE',
    },
  };

  return (
    <div style={styles.homePage}>
      <h1>Welcome to Home Page</h1>
    </div>
  );
}

export default HomePage;
