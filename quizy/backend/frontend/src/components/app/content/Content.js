import React, { useState, useEffect } from 'react';

import { connect } from 'react-redux';
import { quizzesFetchData } from '../../../reducers/quizzes';

import s from './Content.module.css';
import Quiz from './Quiz/Quiz'

const Content = (props) => {

    useEffect(() => {
        props.fetchData('/api/v1/quizzes');
    });

    return (
        <div className="content">
            <div className={"col-md-6 " + s.content}>
                   {
                        props.quizzes.map(quiz => (
                            <div key={quiz.id}>
                                <Quiz title={quiz.title} creator={quiz.creator} description={quiz.description} />
                            </div>
                        ))
                    }
            </div>
        </div>
    )
}

const mapStateToProps = state => {
    return {
        quizzes: state.quizzes
    }
}

const mapDispatchToProps = dispatch => {
    return {
        fetchData: url => dispatch(quizzesFetchData(url))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Content);
