
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { AdminPage } from '../admin/admin';
@Component({
  selector: 'page-login',
  templateUrl: 'login.html'
})
export class LoginPage {

  constructor(public navCtrl: NavController) {
  }
  
  goToAdmin(params){
    if (!params) params = {};
    this.navCtrl.setRoot(AdminPage);
  }
}

 