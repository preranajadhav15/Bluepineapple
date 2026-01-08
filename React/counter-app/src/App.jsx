import { useState } from "react";

function App() {
  const[count,setCount]=useState(0);
  return(
    <div style={{display:"flex",justifyContent:"center",width:"100vw",alignItems:"center",height:"100hv",flexDirection:"column"}}>
      <h2>Counter: {count}</h2>
      <button onClick={()=>setCount(count+1)}>Click Here</button>
    </div>
  );
}
export default App;