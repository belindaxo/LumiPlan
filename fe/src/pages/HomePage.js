import React, { useState } from 'react';
import logo from '../logos/logo.png';
import DatePicker from 'react-datepicker';
import { useNavigate } from 'react-router-dom';
import 'react-datepicker/dist/react-datepicker.css';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';


function HomePage() {
  const [tasks, setTasks] = useState([]);
  const [showCompletedTasks, setShowCompletedTasks] = useState(false);
  const [newTask, setNewTask] = useState({ title: '', deadline: new Date(), completed: false });
  const [showModal, setShowModal] = useState(false);
  const navigate = useNavigate();
  const localizer = momentLocalizer(moment); // Add this line
  const [calendarView, setCalendarView] = useState('month'); // Add this line



  const addTask = () => {
    setTasks([...tasks, newTask]);
    setNewTask({ title: '',  deadline: new Date(), completed: false }); // Reset new task state
    setShowModal(false); // Close modal
  };
  const handleChatWithLumi = () => {
  console.log("Chat with Lumi feature coming soon!");
  // Or, use an alert to inform the user
  // alert("Chat with Lumi feature coming soon!");
};


  const toggleTaskCompletion = (index) => {
    const newTasks = [...tasks];
    newTasks[index].completed = !newTasks[index].completed;
    setTasks(newTasks);
  };

  const toggleViewCompleted = () => {
    setShowCompletedTasks(!showCompletedTasks);
  };

  const handleLogout = () => {
    // Perform any additional cleanup actions if needed
    // Redirect to the default page
    navigate('/'); // Navigate to the default page
  };

  const deleteTask = (index) => {
    const newTasks = tasks.filter((_, taskIndex) => taskIndex !== index);
    setTasks(newTasks);
  };

  const styles = {
    container: {
        display: 'flex',
        flexDirection: 'row',
        height: 'calc(100vh - 80px)', // Adjusted height considering the header's height
        overflow: 'hidden', // Prevent scrolling within the container
        width: '100%',
        fontFamily: "'Dangrek', cursive",

      },
    header: {
      display: 'flex',
      alignItems: 'center',
      backgroundColor: '#173155',
      color: '#F1FAEE',
      padding: '20px',
      fontFamily: "'Dangrek', cursive",
      width: '96.9%',
      height: '40px',
    },
    logo: {
      height: '50px',
      marginRight: '10px',
    },
    sidebar: {
      width: '20%',
      backgroundColor: '#F1FAEE',
      padding: '20px',
      overflowY: 'auto',
      display: 'flex',
      flexDirection: 'column',
      height: 'calc(100vh - 100px)', // Adjusted height considering the header's height
    },
    mainContent: {
      flex: 1,
      backgroundColor: '#A8DADC',
      padding: '20px',
      overflowY: 'auto',
      fontFamily: "'Dangrek', cursive",

    },
    taskItem: {
      border: '2px solid #173155', // Dark blue outline
      backgroundColor: '#F1FAEE', // Light fill
      color: 'black',
      padding: '10px',
      marginBottom: '10px',
      borderRadius: '5px',
      display: 'flex',
      alignItems: 'center',
    },
    button: {
      marginBottom: '20px',
      backgroundColor: '#E63946', // Light pink color
      fontFamily: "'Dangrek', cursive", // Cutesy bubble font
      padding: '10px 20px',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
    },
    toggleViewButton: {
      marginTop: 'auto', // Pushes the button to the bottom of the sidebar
      backgroundColor: '#FAD2E1', // Light pink color
      fontFamily: "'Dangrek', cursive", // Cutesy bubble font
      padding: '10px 20px',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
    },
    tasksContainer: {
        flex: 1,
        overflowY: 'auto',
        paddingTop: '20px',
        paddingBottom: '20px',
      },
      modalOverlay: {
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 1000,
      },
      modalContent: {
        backgroundColor: '#F1FAEE',
        padding: '20px',
        borderRadius: '5px',
        display: 'flex',
        flexDirection: 'column',
        fontFamily: "'Dangrek', cursive",
      },
      modalInput: {
        marginBottom: '10px',
        padding: '10px',
        border: '1px solid #ccc',
        borderRadius: '4px',
        fontFamily: "'Dangrek', cursive",
      },
  };

  return (
    <div>
      {/* Header section */}
      <div style={{...styles.header, justifyContent: 'space-between'}}>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <img src={logo} alt="LumiPlan Logo" style={styles.logo} />
          <span>LumiPlan</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', marginTop: '20px' }}>
          {/* Chat with Lumi button */}
          <button style={{ ...styles.button, height: '44px', display: 'flex', alignItems: 'center', marginRight: '10px' }} onClick={handleChatWithLumi}>
            <img src={logo} alt="Chat with Lumi" style={{ height: '30px', marginRight: '10px' }} /> Chat with Lumi
          </button>
          {/* Logout button */}
          <button style={styles.button} onClick={handleLogout}>Logout</button>
        </div>
      </div>
  
      {/* Main content and sidebar */}
      <div style={styles.container}>
        <div style={styles.sidebar}>
          {/* Fixed Add Task Button */}
          <button style={styles.button} onClick={() => setShowModal(true)}>Add Task</button>
  
          {/* Scrollable Task List */}
          <div style={styles.tasksContainer}>
            {tasks.filter(task => task.completed === showCompletedTasks).map((task, index) => (
              <div key={index} style={styles.taskItem}>
                <input
                  type="checkbox"
                  checked={task.completed}
                  onChange={() => toggleTaskCompletion(index)}
                />
                {task.title} - {new Date(task.deadline).toLocaleString()}
                <button style={{ ...styles.button, marginLeft: 'auto', padding: '5px', height: '30px', display: 'flex', alignItems: 'center', fontSize: '0.8rem', margin: '5px' }} onClick={() => deleteTask(index)}>X</button>
              </div>
            ))}
          </div>
  
          {/* Fixed See Completed Tasks Button */}
          <button style={{ ...styles.button, marginTop: '10px' }} onClick={toggleViewCompleted}>
            {showCompletedTasks ? 'See Uncompleted Tasks' : 'See Completed Tasks'}
          </button>
        </div>
  
        <div style={styles.mainContent}>
          {/* Calendar Component */}
          <Calendar
            localizer={localizer}
            events={tasks.map(task => ({
              title: task.title,
              start: new Date(task.deadline),
              end: new Date(task.deadline),
              allDay: false
            }))}
            startAccessor="start"
            endAccessor="end"
            style={{ height: 500, marginTop: '10px' }}
            view={calendarView}
            onView={view => setCalendarView(view)}
          />
        </div>
      </div>
  
      {/* Add Task Modal - This is the part you asked about, positioned just before the return statement's closing </div> */}
      {showModal && (
        <div style={styles.modalOverlay}>
          <div style={styles.modalContent}>
            <h2 style={{ fontFamily: "'Dangrek', cursive" }}>Add a New Task</h2>
            <input
              type="text"
              value={newTask.title}
              onChange={(e) => setNewTask({ ...newTask, title: e.target.value, deadline: newTask.deadline, completed: newTask.completed })}
              placeholder="Task Title"
              style={styles.modalInput}
            />
            <DatePicker
              selected={newTask.deadline}
              onChange={(date) => setNewTask({ ...newTask, deadline: date })}
              showTimeSelect
              timeFormat="HH:mm"
              timeIntervals={15}
              dateFormat="MMMM d, yyyy h:mm aa"
              style={styles.modalInput}
            />
            <button style={{ ...styles.button, marginTop: '20px' }} onClick={() => { addTask(); setShowModal(false); }}>Submit</button>
            <button style={{ ...styles.button, marginTop: '10px' }} onClick={() => setShowModal(false)}>Cancel</button>
          </div>
        </div>
      )}
    </div>
  );
      }
  

export default HomePage;