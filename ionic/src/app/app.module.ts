import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';
import { AdminPage,ModalContentPage } from '../pages/admin/admin';
import { LoginPage } from '../pages/login/login';
import { SupervisorPage } from '../pages/supervisor/supervisor';


import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { UbicacionProvider } from '../providers/ubicacion/ubicacion';
import { UsuarioProvider } from '../providers/usuario/usuario';
import { MonitoreoProvider } from '../providers/monitoreo/monitoreo';

@NgModule({
  declarations: [
    MyApp,
    AdminPage,
    LoginPage,
    SupervisorPage,
    ModalContentPage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    AdminPage,
    LoginPage,
    SupervisorPage,
    ModalContentPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    UbicacionProvider,
    UsuarioProvider,
    MonitoreoProvider
  ]
})
export class AppModule {}