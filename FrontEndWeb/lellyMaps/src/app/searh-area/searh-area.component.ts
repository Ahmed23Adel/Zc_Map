import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Observable, Subscription } from 'rxjs';

@Component({
  selector: 'app-searh-area',
  templateUrl: './searh-area.component.html',
  styleUrls: ['./searh-area.component.scss']
})
export class SearhAreaComponent {
  ///////////////////////////////////////////////
  //// send signal to parent to tell zc map to catch any click
  @Output() selectFromChild = new EventEmitter();
  @Output() selectToChild = new EventEmitter();
  ///////////////////////////////////////////////
  ///////////////////////////////////////////////
  //////// get value gotten from user to print in the textbox
  @Input() msgSrchAreaFromChild:any = "xxx";
  @Input() msgSrchAreaToChild:any = "yyy";
  ///////////////////////////////////////////////
  ///////////////////////////////////////////////
  ////////// final values set by user to send it to parent, 
  ///// which he should send it to zc map to call an api
  @Output() FinalFromChild = new EventEmitter()
  @Output() FinalToChild = new EventEmitter()
  @Output() FinalCheckedChild = new EventEmitter()
  @Output() FinalSignal = new EventEmitter()
  @Output() FinalAlgoChild = new EventEmitter()
  ///////////////////////////////////////////////
  ///// final alg chosen by user
  final_alg:string = ""

  isChecked:boolean = true;
  //// to see if they should collapse the serch area
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
    /**
     * collapse the search area
     */
    this.isExpanded = !this.isExpanded;
    
  }
  
  setAlg(){
    /**
     * find the algorith chosen by the user
     */
    const astar_ = document.getElementById("item0")as HTMLInputElement;
    const astar = astar_.checked;

    const ucs_ = document.getElementById("item1")as HTMLInputElement;
    const ucs = ucs_.checked;

    const greedy_ = document.getElementById("item2")as HTMLInputElement;
    const greedy = greedy_.checked;
    
    const bfs_ = document.getElementById("item3")as HTMLInputElement;
    const bfs = bfs_.checked;

    const dfs_ = document.getElementById("item4")as HTMLInputElement;
    const dfs = dfs_.checked;

    const ids_ = document.getElementById("item5")as HTMLInputElement;
    const ids = ids_.checked;

    const dls_ = document.getElementById("item6")as HTMLInputElement;
    const dls = dls_.checked;

    const hill_climging_ = document.getElementById("item7")as HTMLInputElement;
    const hill_climging = hill_climging_.checked;

    const simulate_ann_ = document.getElementById("item8")as HTMLInputElement;
    const simulate_ann = simulate_ann_.checked;
    console.log("What is checked?")
    console.log(bfs, dfs,dls,ids,greedy,ucs,astar)
    this.final_alg = "astar"
    if (bfs)
       this.final_alg = "bfs"
    if (dfs)
       this.final_alg = "dfs"
    if (dls)
       this.final_alg = "dls"
    if (ids)
       this.final_alg = "ids"
    if (greedy)
       this.final_alg = "greedy"
    if (ucs)
       this.final_alg = "ucs"
    if (astar)
       this.final_alg = "astar"

  }

  sendChooseFromToParent(){
    this.selectFromChild.emit("from")
    
  }
  sendChooseToToParent(){
    this.selectToChild.emit("to")
  }
  

  SearchSubmit(){
    this.setAlg();
    this.FinalFromChild.emit(this.msgSrchAreaFromChild);
    this.FinalToChild.emit(this.msgSrchAreaToChild);
    this.FinalCheckedChild.emit(this.isChecked);
    this.FinalAlgoChild.emit(this.final_alg);
    this.FinalSignal.emit();

  }
}
