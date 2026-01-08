import { useState,useEffect } from 'react'
import './App.css'

function App() {
  const [user, setUser] = useState(null)
  useEffect(()=>{
    fetch("https://jsonplaceholder.typicode.com/users")
    .then((response)=>response.json())
    .then((data)=> {
      setUser(data[0])
    })
    .catch((error)=> {
      console.error("Error fetching user:",error)
    })
  },[])

  return (
    <div style={{
      display:"flex",
      flexDirection:"column",
      justifyContent:"center",
      alignItems:"center",
      height:"100vh",
      gap:"20px",
      fontFamily:"sans-serif"
    }}>
      <h2>Random User</h2>
      {user ? (
        <div>
          <p><strong>Name:</strong>{user.name}</p>
          <p><strong>Email:</strong>{user.email}</p>
        </div>
      ):(
        <p>Loading user...</p>
      )}
    </div>
  )
}
export default App
