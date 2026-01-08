import { useState } from 'react'
import TodoList from './Todo'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{
      display:"flex",
      justifyContent:"center",
      flexDirection:"column",
      fontFamily:"sans-serif",
      height:"100vh",
      alignContent:"center"
    }}><TodoList/></div>
  );
}

export default App
