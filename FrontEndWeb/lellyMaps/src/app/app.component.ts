import { Component } from '@angular/core';
import { SolutionBackedService } from './solution-backed.service';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  msgZcMapFrom = "-1"//if +1 don't catch mouse, if -1 catch it
  msgZcMapTo = "-1"//if +1 don't catch mouse, if -1 catch it
  msgSearchAreaFrom = ""
  msgSearchAreaTo = ""
  valueFromParent = "0,0";
  valueToParent = "0,0";

  FinalFrom = ""
  FinalTo = ""
  FinalChecked = ""


  title = 'lellyMaps';
  signalFromSearchArea = ""

  FinalFromParent = ""
  FinalToParent = ""
  FinalCheckedParent = ""
  FinalAloParent = ""

  FinalFromToZcMap: any;
  FinalToToZcMap: any;
  FinalAlgToZcMap: any;
  FinalCheckedToZcMap: any;

  constructor(private solServiceData:SolutionBackedService){}
  // _url = "http://127.0.0.1:8000/?alg=astar&col1=5&col2=20&format=json&row1=1&row2=1&type1=cord&type2=cord"
  // constructor(private _http:HTTPClient){}

  catchFrom(){
    console.log("Ahmexcd")
    this.msgZcMapFrom = "+1"
  }

  catchTo(){
    console.log("catchTo")
    this.msgZcMapTo = "+1"
  }

  userSelectedFrom(ev:any){
    this.valueFromParent = ev;
    console.log("User Selected From", this.valueFromParent);
    console.log("User Selected To", this.valueToParent)
    this.msgZcMapTo = "-1";
    this.msgZcMapFrom = "-1";
    this.msgSearchAreaFrom = this.valueFromParent;
  }

  userSelectedTo(ev:any){
    this.valueToParent = ev;
    console.log("User Selected From", this.valueFromParent);
    console.log("User Selected To", this.valueToParent)
    this.msgZcMapTo = "-1";
    this.msgZcMapFrom = "-1";
    this.msgSearchAreaTo = this.valueToParent;
    
  }

  SearchApi(){
    
    // console.log("Search", this.FinalCheckedParent)
    // console.log("Search", this.FinalFromParent)
    // console.log("Search", this.FinalToParent)
    // console.log("Search", this.FinalAloParent)
    this.notifyClick();
  //   this.solServiceData.getSolution(this.FinalFromParent, this.FinalToParent,this.FinalAloParent ).subscribe(
  //     serviceData=>{

  //       for(let i=0; i<serviceData.alg_output.length; i++){
  //         let current_id = serviceData.alg_output[i];
  //         let current_ele = document.getElementById(current_id)!
  //         console.log(current_ele)
  //       }
  //     }
  //   )
  }

  eventsSubject: Subject<void> = new Subject<void>();

  notifyClick() {
    console.log("notifyClick")

    this.FinalFromToZcMap =this.FinalFromParent ;
    this.FinalToToZcMap = this.FinalToParent;
    this.FinalAlgToZcMap = this.FinalAloParent;
    this.FinalCheckedToZcMap = this.FinalCheckedParent;

    console.log("Search", this.FinalFromToZcMap)
    console.log("Search", this.FinalToToZcMap)
    console.log("Search", this.FinalAlgToZcMap)
    console.log("Search", this.FinalCheckedToZcMap)
    this.eventsSubject.next();
  }
}
