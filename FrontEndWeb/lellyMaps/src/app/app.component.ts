import { Component } from '@angular/core';

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


  title = 'lellyMaps';
  signalFromSearchArea = ""

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
}
