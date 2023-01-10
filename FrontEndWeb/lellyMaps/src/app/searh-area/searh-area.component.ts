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

  //////////////////////////////////////////////////
  ///////////////emitter for sending singal to RL
  //////////////////////////////////////////////////
  @Output() ShowRL = new EventEmitter()
  ///// final alg chosen by user
  final_alg:string = ""

  isChecked:boolean = true;
  //// to see if they should collapse the serch area
  isExpanded = true;
  userHistory:string[] = ['D(D2)', 'w(D)', 'D(D1)', 'e(D)', 'S(D)', 'AC(D)', 'AC(G20)', 'AC(G19)', 'AC(G18)', 
                  'AC(G12)', 'AC(Zone B)', 'AC(G11)', 'AC(G10)', 'AC(G9)', 'AC(G8)', 'AC(Toilets)', 'AC(G6, security room)', 
                  'AC(G7)', 'AC(ATM)', 'AC(Security room)', 'AC(G6)', 'AC(D1)', 'AC(G1)', 'AC(F)', 'AC(G13)', 'AC(G5)', 
                  'AC(cats office)', 'AC(G14)', 'AC(G15)', 'AC(Locker)', 'N(elevator)', 'H(D2)', 'H(Toilet)', 'N(D1)', 'H(Mosque)',
                  'H(class4)', 'H(class3)', 'N(Toilet)', 'H(Biology lab)', 'H(class2)', 'H(class1)', 'H(D1)', 'N(G004)', 
                  'N(Meeting room)', 'H(stairs)', 'N(Microscope)', 'N(G021)', 'N(G022)', 'H(elevator)', 'H(chemistry lab)', 
                  'N(G018)', 'H(office)', 'N(communication)', 'H(D3)', 'O(D)', 'CC(D1)','helmy', 'nano', 'service',
                   'culture complex', 'one stop', 'onestop', 'dorms', 'engineering', 'workshop', 'academic'];

  

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
    if (hill_climging)
       this.final_alg = "hillclimbing"
    if (simulate_ann)
       this.final_alg = "simulatedannealing"


  }

  sendChooseFromToParent(){
    this.selectFromChild.emit("from")
    
  }
  sendChooseToToParent(){
    this.selectToChild.emit("to")
  }
  

  SearchSubmit(){
    this.setAlg();
    console.log("this.final_alg",this.final_alg)
    this.FinalFromChild.emit(this.msgSrchAreaFromChild);
    this.FinalToChild.emit(this.msgSrchAreaToChild);
    this.FinalCheckedChild.emit(this.isChecked);
    this.FinalAlgoChild.emit(this.final_alg);
    this.FinalSignal.emit();

  }

  show_rl(){
   this.ShowRL.emit()
  }
}
