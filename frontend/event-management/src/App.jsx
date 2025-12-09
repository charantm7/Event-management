import React, { useState, useEffect } from "react";

function App() {
  const [info, setInfo] = useState(null);
  //

  async function getInfo() {
    try {
      const req = await fetch("http://127.0.0.1:8000/");

      const response = await req.json();

      setInfo(response);

      console.log(response);
    } catch (e) {
      console.log("request failed");
    }
  }

  return (
    <div className="flex justify-center items-center ">
      <h1 className="">App</h1>
      <button onClick={() => getInfo()}>Click me</button>
      <pre>{info}</pre>
    </div>
  );
}

export default App;
