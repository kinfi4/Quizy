import React from 'react';
import s from './Header.module.css';
import Navigation from './navigation/Navigation';


const Header = () => {
    return (
         <header className={s.header}>
             <div className={s.logo}>Quizy</div>
             <Navigation />
         </header>
    )
}

export default Header;