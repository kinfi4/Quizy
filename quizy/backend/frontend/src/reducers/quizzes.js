const QUIZZES_GET_ALL = 'QUIZZES_GET_ALL'

export function quizzesFetchData(url){
    return (dispatch) => {
        fetch(url)
            .then(response => {
                if(!response.ok){
                    throw new Error(response.statusText);
                }
                return response;
            })
            .then(response => {
                return response.json()
            })
            .then(quizzes => dispatch({ type: QUIZZES_GET_ALL, quizzes: quizzes }))
    }
}


export function quizzes(state=[], action){
    switch(action.type){
        case QUIZZES_GET_ALL:
            return action.quizzes;
        default:
            return state;
    }
}
