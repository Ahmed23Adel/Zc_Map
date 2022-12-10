import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-searh-area',
  templateUrl: './searh-area.component.html',
  styleUrls: ['./searh-area.component.scss']
})
export class SearhAreaComponent {

  @Output() selectFromChild = new EventEmitter();
  @Output() selectToChild = new EventEmitter();

  @Input() msgSrchAreaFromChild:any = "xxx";
  @Input() msgSrchAreaToChild:any = "yyy";


  filp:boolean = true;

  isChecked:boolean = true;

  isExpanded = true;
  userHistory:string[] = [ 'D(D2)', 'w(D)', 'D(D1)', 'e(D)', 'S(D)', 'AC(D)', 'AC(G20)', 'AC(G19)', 'AC(G18)',
      'AC(G12)', 'AC(Zone B)', 'AC(G11)', 'AC(Zone B)', 'AC(G10)', 'AC(Zone B)', 'AC(G9)', 'AC(Zone B)', 'A',
    'C(G8)', 'AC(Toilets)', 'AC(G6, security room)', 'AC(G11)', 'AC(Zone B)', 'AC(G7)', 'AC(D)', 'AC(ATM)',
      'AC(Security room)', 'AC(G12)', 'AC(Zone B)', 'AC(G6)', 'AC(D1)', 'AC(G1)', 'AC(F)', 'AC(F)', 'AC(F)', 
      'AC(G13)', 'AC(Zone B)', 'AC(G5)', 'AC(cats office)', 'AC(F)', 'AC(F)', 'AC(F)', 'AC(G14)', 'AC(G14)', 
      'AC(F)', 'AC(F)', 'AC(F)', 'AC(G15)', 'AC(G15)', 'AC(F)', 'AC(F)', 'AC(F)', 'AC(Locker)', 'AC(Locker)', 
      'AC(Locker)', 'AC(Locker)', 'AC(Locker)', 'H(D2)', 'N(D1)', 'H(D1)', 'H(D3)', 'O(D)', 'CC(D1)','ac', 'w', 
      'e', 'd','o','cc','s','n','h','helmy','nano','nano','culture complex','one stop','onestop','dorms','engineering','workshop','academic'];
  expand(){
    this.isExpanded = !this.isExpanded;
    const ucs_ = document.getElementById("item1")as HTMLInputElement;
    const ucs = ucs_.checked;

    console.log(this.msgSrchAreaFromChild)
    console.log(this.msgSrchAreaToChild)
  }
   

  sendChooseFromToParent(){
    console.log("Send from")
    const  chooseFromEle= window.document.getElementById("choose-from")!
    this.selectFromChild.emit("from")
    // if(this.filp){
    //   chooseFromEle.style.borderBlockStyle = "dotted";
    //   chooseFromEle.style.borderWidth = "5px";
    //   this.filp = !this.filp;
    // }else{
    //   chooseFromEle.style.borderBlockStyle = "solid";
    //   chooseFromEle.style.borderWidth = "1px";
    //   this.filp = !this.filp;
    // }
    
  }
  sendChooseToToParent(){
    console.log("SearchArea: Send to")
    this.selectToChild.emit("to")
    // const  chooseFromEle= window.document.getElementById("choose-to")!
    // if(this.filp){
    //   chooseFromEle.style.borderBlockStyle = "dotted";
    //   chooseFromEle.style.borderWidth = "5px";
    //   this.filp = !this.filp;
    // }else{
    //   chooseFromEle.style.borderBlockStyle = "solid";
    //   chooseFromEle.style.borderWidth = "1px";
    //   this.filp = !this.filp;
    // }
  }
  
  // checkCheckBoxvalue(event:any){
  //   this.isShowSteps = event.checked;
  // }

  SearchSubmit(){
    console.log(this.msgSrchAreaFromChild);
    console.log(this.msgSrchAreaToChild);
    console.log(this.isChecked);

  }
}
