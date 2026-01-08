import { useRef } from 'react'
import './App.css'

function App() {
  const input=useRef(null)
  const handleFocus=()=> {
    input.current.focus()
  };


  return (
    <div style={{
      display:"flex",
      justifyContent:"center",
      flexDirection:"column",
      fontFamily:"sans-serif",
      alignItems:"center",
      gap:"20px",
      height:"100vh"
      }}>
    <input ref={input} type='text' placeholder='Type here' style={{padding:"8px",fontSize:"16px",width:"200px"}}/>
    <button onClick={handleFocus} 
    style={{
      padding:"8px 16px",
      fontSize:"16px",
      cursor:"pointer"
      }}>Focus Input</button>
      </div>
  );
}

export default App





