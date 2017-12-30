import { Component } from '@angular/core';

/**
 * Generated class for the FooterAppComponent component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'footer-app',
  templateUrl: 'footer-app.html'
})
export class FooterAppComponent {

  text: string;

  constructor() {
    console.log('Hello FooterAppComponent Component');
    this.text = 'Hello World';
  }

}
