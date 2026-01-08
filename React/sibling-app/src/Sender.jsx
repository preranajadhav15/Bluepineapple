function Sender({setMessage}) {
    return (
        <div>
            <input type="text" placeholder="message" onChange={(e)=>setMessage(e.target.value)}/>
        </div>
    );
}
export default Sender