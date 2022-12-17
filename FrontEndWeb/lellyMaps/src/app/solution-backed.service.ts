import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { IAlgoSolutoin } from './responseApi/IAlgoSolution';



@Injectable({
  providedIn: 'root'
})
export class SolutionBackedService {

  // _url = "http://127.0.0.1:8000/?alg=astar&col1=5&col2=20&format=json&row1=1&row2=1&type1=cord&type2=cord"
  _url = "http://127.0.0.1:8000"
  constructor(private _http: HttpClient) { }

  getSolution(from:any, to:any, alg: any)
  {
    // from can be on form (2,6) or Ac or N(G19)
    let type1= "cord"
    let type2= "cord"
    let row1, col1, row2, col2;
    let regexp = new RegExp('\d*,\d*')
    if( (regexp.test(from))  )
    {
      // then it's on form of 1,4
      row1 = from.split(",")[0];
      col1 = from.split(",")[1];
      type1 = 'cord';
      console.log("u11","row1, col1",row1, col1);
    }
    else{
      // it's on form of Ac(G19)
      row1 = from;
      col1 = "empty";
      type1 = "pos"
      console.log("u11","row1, col1",type1, row1, col1);

    }

    if( (regexp.test(to))  )
    {
      // then it's on form of 1,4
      row2 = to.split(",")[0];
      col2 = to.split(",")[1];
      type2 = 'cord';
      console.log("u1","row2, col2",type2, row2, col2);
    }
    else{
      row2 = to;
      col2 = "empty";
      type2 = "pos"
      console.log("u1","row2, col2",type2, row2, col2);
    }
    console.log("u1122", alg);

    let queryParams = new HttpParams();
    queryParams = queryParams.append("row1",row1);
    queryParams = queryParams.append("col1",col1);
    queryParams = queryParams.append("row2",row2);
    queryParams = queryParams.append("col2",col2);
    queryParams = queryParams.append("alg",alg);
    queryParams = queryParams.append("type1",type1);
    queryParams = queryParams.append("type2",type2);
    queryParams = queryParams.append("format","json");

    return this._http.get<IAlgoSolutoin>(this._url, {params:queryParams})

  }
}
