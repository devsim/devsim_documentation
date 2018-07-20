#!/usr/bin/perl
use strict;
my $EPSILON = 1e-10;

sub getcenter
{
  my $x1 = shift;
  my $y1 = shift;
  my $x2 = shift;
  my $y2 = shift;
  my $x3 = shift;
  my $y3 = shift;

  my $xcenter;
  my $ycenter;

  if (abs($y2-$y1) < $EPSILON) {
      my $m2 = - ($x3-$x2) / ($y3-$y2);
      my $mx2 = ($x2 + $x3) / 2.0;
      my $my2 = ($y2 + $y3) / 2.0;
      $xcenter = ($x2 + $x1) / 2.0;
      $ycenter = $m2 * ($xcenter - $mx2) + $my2;
  }
  elsif (abs($y3-$y2) < $EPSILON) {
      my $m1 = - ($x2-$x1) / ($y2-$y1);
      my $mx1 = ($x1 + $x2) / 2.0;
      my $my1 = ($y1 + $y2) / 2.0;
      $xcenter = ($x3 + $x2) / 2.0;
      $ycenter = $m1 * ($xcenter - $mx1) + $my1;
  }
  else
  {
    my $m1 = - ($x2-$x1) / ($y2-$y1);
    my $m2 = - ($x3-$x2) / ($y3-$y2);
    my $mx1 = ($x1 + $x2) / 2.0;
    my $mx2 = ($x2 + $x3) / 2.0;
    my $my1 = ($y1 + $y2) / 2.0;
    my $my2 = ($y2 + $y3) / 2.0;
    $xcenter = ($m1 * $mx1 - $m2 * $mx2 + $my2 - $my1) / ($m1 - $m2);
    $ycenter = $m1 * ($xcenter - $mx1) + $my1;
  }
  return ($xcenter, $ycenter);
}


my $xc = 10;
my $yc = 10;
my $rad = 10;

my $sides = 5;


my $pi = 4*atan2(1,1);
print "$pi\n";

#my $rot = $pi/$sides;
my $rot = 0;

my $angleincrement = 2*$pi / $sides;

my @xcoords;
my @ycoords;

print "Coordinates\n";
for (my $i = 0; $i < $sides; $i++)
{
  my $angle = $rot + $i * $angleincrement;
  my $x = $xc + $rad * cos($angle);
  my $y = $yc + $rad * sin($angle);
  print "$x $y\n";
  push @xcoords, $x;
  push @ycoords, $y;
}
print "Triangle Centers\n";

for (my $i = 0; $i < $sides; $i++)
{
  my $j = ($i + 1) % $sides;
  my @center = getcenter($xc, $yc, $xcoords[$i], $ycoords[$i], $xcoords[$j], $ycoords[$j]);
  print "$center[0] $center[1]\n";
}
