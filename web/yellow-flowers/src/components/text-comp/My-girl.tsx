import { useState } from 'react'
import './my-girl.css';
import YourFlowers from '../flowers-comp/Your-flowers';
const arrow = ">>";

function MyGirl() {

    const frases: string[] = [
        "Hola mi niña bonita...",
        "Se que no nos podemos ver hoy...",
        "y esta distancia es complicada...",
        "pero no dejaría que...",
        "pase este día...",
        "sin darte tus...",
        "Florecitas amarillas"
    ];
    const [count, setCount] = useState(0);

    const [isShown, setIsShown] = useState(false);

    function  handleClick() {
        // 👇️ toggle shown state
        console.log('It works')
        setIsShown(current => !current);
    };

    return(
    <>
        {isShown && <YourFlowers />}
        <h2>{ frases[count] }</h2>
        <div className="card">
            <button onClick={
                () => {
                    if (count >= frases.length - 1) {
                        handleClick();
                    }else{
                        setCount((count) => count + 1);
                    }
                }
            }>
            { arrow }
            </button>
        </div>
    </>
    )
}

export default MyGirl;