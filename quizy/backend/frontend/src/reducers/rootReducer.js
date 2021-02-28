import { combineReducers } from 'redux';
import { quizzes } from './quizzes';

const rootReducer = combineReducers({
    quizzes: quizzes 
});

export default rootReducer;
