import { Component } from '@angular/core';
import { GreetService }       from './greetService';
import { UserData }    from './userData';

@Component({
  selector: 'greet-form',
  templateUrl: 'app/greet-form.component.html',
  providers : [GreetService]
})
export class GreetFormComponent {

  constructor (private greetService: GreetService){}
  greeting = 'Привет! Введи свое имя.';
  submitted = false;
  onSubmit() { this.submitted = true;  }
  active = true;
  userdata : UserData;
  getGreeting(name:string) {
    this.greetService.getGreetings(name)
    .subscribe(data => this.userdata = data);
    this.greeting = 'Добро пожаловать снова';
  }
}
