import { Component, ViewChild } from '@angular/core';
import { Platform, Nav } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { AdminPage } from '../pages/admin/admin';


import { LoginPage } from '../pages/login/login';

import { DetallesPage } from '../pages/detalles/detalles';



@Component({
  templateUrl: 'app.html'
})
export class MyApp {
  @ViewChild(Nav) navCtrl: Nav;
    rootPage:any = LoginPage;

  constructor(platform: Platform, statusBar: StatusBar, splashScreen: SplashScreen) {
    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      statusBar.styleDefault();
      splashScreen.hide();
    });
  }
  goToAdmin(params){
    if (!params) params = {};
    this.navCtrl.setRoot(AdminPage);
  }

  goToDetalles(params){
    if (!params) params = {};
    this.navCtrl.setRoot(DetallesPage);
  }

}
