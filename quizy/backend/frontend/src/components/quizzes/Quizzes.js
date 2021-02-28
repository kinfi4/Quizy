import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux'
import { quizzesFetchData } from './../../reducers/quizzes';


export class Quizzes extends Component{
    componentDidMount(){        
        this.props.fetchData('/api/v1/quizzes');
    }
    
    render(){
        return (
            <Fragment>
                <h2>Quizzes</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Code</th>
                            <th>Title</th>
                            <th>Creator</th>
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.props.quizzes.map(quiz => {
                                return (
                                    <tr key={quiz.id}>
                                        <td>{quiz.code}</td>
                                        <td>{quiz.title}</td>
                                        <td>{quiz.creator.username}</td>
                                        <td><button className="btn btn-danger btn-sm">Delete</button></td>
                                    </tr>
                                )
                            })
                        }

                    </tbody>
                </table>
                </Fragment>
            )
    
    }
}


const mapStateToProps = state => {
    return {
        quizzes: state.quizzes
    }
}

const mapDispatchToProps = dispatch => {
    return {
        fetchData: url => {dispatch(quizzesFetchData(url))}
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Quizzes);










