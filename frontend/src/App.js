import "./App.css";
import CardView from "./Components/CardView";
import "bootstrap/dist/css/bootstrap.min.css";
import NavBar from "./Components/NavBar";

function App() {
  return (
    <div className="App">
      <NavBar></NavBar>
      <CardView></CardView>
      <CardView></CardView>
      <CardView></CardView>

    </div>
  );
}

export default App;
