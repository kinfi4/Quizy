import React from 'react';
import s from './Quiz.module.css';

const Quiz = (props) => {
    return (
        <div className={s.quiz}>
            <div className={s.caption}>{props.title}</div>
            <div className={s.username}>@{props.creator.username}</div>
            <div className={s.description}>{props.description}</div>
        </div>
    )
}

export default Quiz;