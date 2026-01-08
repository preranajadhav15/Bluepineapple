import { useState } from 'react'
import Sender from './Sender'
import Receiver from './Receiver'

import './App.css'

function App() {
  const [message,setMessage]=useState("")

  return (
    <>
      <div style={{display:"flex",justifyContent:"center",height:"100vh",width:"100wh",alignItems:"center",gap: "20px"}}>
        <h3>Passing data between two sliblings.</h3>
        <Sender setMessage={setMessage}/>
        <Receiver message={message}/>
      </div>
    </>
  );
}

export default App
