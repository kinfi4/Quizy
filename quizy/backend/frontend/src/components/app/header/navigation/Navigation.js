import React from 'react';
import s from './Navigation.module.css';


const Navigation = () => {
    return (
        <div className={s.nav_block}>
            <button className={"btn btn-info " + s.create_quiz_btn}>Create Quiz</button>
            <button className={"btn btn-info " + s.sing_in_btn}>Sing in</button>
        </div>
    )
}

export default Navigation;