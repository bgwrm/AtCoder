using System;
class Program
{
	static void Main(string[] args)
	{
        int a = int.Parse(Console.ReadLine());
        string[] bc = Console.ReadLine().Split(" ");
        int b = int.Parse(bc[0]);
        int c = int.Parse(bc[1]);
        string s = Console.ReadLine();

        Console.WriteLine($"{a+b+c} {s}");
	}
}