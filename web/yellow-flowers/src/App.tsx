import './App.css'
import MyGirl from './components/text-comp/My-girl'


import imagesData from './assets/web-images.json'

const home_logo = imagesData['images-data'][0];

function App() {

  return (
    <>
      <div>
        <a href="#" target="_blank">
          <img src={ home_logo.src } className="logo react" key={ home_logo.id_key } alt="React logo" />
        </a>
      </div>
      <MyGirl/>
      <p className="read-the-docs">
        Tu dale a la flechita miamor<br/><br/>
        <small>By: Amor47</small>
      </p>
    </>
  )
}

export default App
