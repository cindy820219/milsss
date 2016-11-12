#!/usr/bin/perl 

my $mw = new MainWindow(-title=>'我的第一個Tk程式');

$mw->geometry('400x50');



my $label = $mw->Label(-text=>'測試文字', -relief =>'sunken', -border =>2);

$label->pack(-side =>'top', -fill =>'both');



my $button = $mw->Button(-text => "關閉程式", -command => sub {$mw->destroy;});

$button->pack(-side =>'top');



MainLoop;
