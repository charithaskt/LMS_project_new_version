import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
       biblios: []
    };
  }

/*
fetch('URL_GOES_HERE', {
   method: 'post',
   headers: new Headers({
     'Authorization': 'Basic '+btoa('username:password'),
     'Content-Type': 'application/x-www-form-urlencoded'
   }),
   body: 'A=1&B=2'
 });
*/

async componentDidMount() {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/v1/biblios/?format=json',    {
                    method: 'get',
                    headers: new Headers({
                         'Authorization': 'Basic '+btoa('charithatsk@gmail.com:admin123'),
                         'Content-Type': 'application/x-www-form-urlencoded'
                    }),
        }); 

        const biblios = await res.json();
	const sorter = (a, b) => {
             return a.biblionumber - b.biblionumber;
        };
        const sortByBiblionumber = arr => {
             arr.sort(sorter);
        };
	if(biblios) {
                 sortByBiblionumber(biblios);
	}
        this.setState({
            biblios
        });
    } catch (e) {
      console.log(e);
    }
}

render() {
    return (
     <div>
      <div className="App">
          <h1>Library Collection List</h1>
      </div>
      <div>
	<table class="indent-40">
	   <thead>
	   <tr>
	    <th>ID</th><th>Title</th><th>Callnumber</th><th>Edition</th><th>Date of publication</th><th>Pages</th><th>Itemtype</th>
	   </tr> 
           </thead>
	   <tbody> 
        {this.state.biblios.map(item => (
          <tr key={item.biblionumber}>
	    <td class="center-text">{item.biblionumber}</td>
            <td><a href={"http://localhost:8000/api/v1/biblio/" + item.biblionumber } target="blank">{item.title}</a></td>
            <td>{item.callnumber}</td>
            <td class="center-text">{item.edition}</td>
            <td class="center-text">{item.copyrightdate}</td>
            <td class="center-text">{item.pages}</td>
            <td class="center-text">{item.itemtype}</td>
          </tr>
        ))}
	</tbody>
	</table>    
       </div>
     </div>
    );
  }
}

export default App; 
