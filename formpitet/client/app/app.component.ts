import { Component }         from '@angular/core';
import { GreetFormComponent } from './greet-form.component';

@Component({
  selector: 'my-app',
  template: '<greet-form></greet-form>',
  directives: [GreetFormComponent]
})
export class AppComponent { }
