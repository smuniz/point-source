; ModuleID = '../src/test35.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test35(i32* %value1, i32* %value2, i32* %value3, i32* %value4, i32* %value5, i32* %value6, i32* %value7, i32* %value8) #0 {
  %1 = alloca i32*, align 8
  %2 = alloca i32*, align 8
  %3 = alloca i32*, align 8
  %4 = alloca i32*, align 8
  %5 = alloca i32*, align 8
  %6 = alloca i32*, align 8
  %7 = alloca i32*, align 8
  %8 = alloca i32*, align 8
  store i32* %value1, i32** %1, align 8
  store i32* %value2, i32** %2, align 8
  store i32* %value3, i32** %3, align 8
  store i32* %value4, i32** %4, align 8
  store i32* %value5, i32** %5, align 8
  store i32* %value6, i32** %6, align 8
  store i32* %value7, i32** %7, align 8
  store i32* %value8, i32** %8, align 8
  %9 = load i32** %1, align 8
  store i32 1, i32* %9, align 4
  %10 = load i32** %2, align 8
  store i32 2, i32* %10, align 4
  %11 = load i32** %3, align 8
  store i32 3, i32* %11, align 4
  %12 = load i32** %4, align 8
  store i32 4, i32* %12, align 4
  %13 = load i32** %5, align 8
  store i32 5, i32* %13, align 4
  %14 = load i32** %6, align 8
  store i32 6, i32* %14, align 4
  %15 = load i32** %7, align 8
  store i32 7, i32* %15, align 4
  %16 = load i32** %8, align 8
  store i32 8, i32* %16, align 4
  ret i32 10
}

; Function Attrs: nounwind
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %value1 = alloca i32, align 4
  %value2 = alloca i32, align 4
  %value3 = alloca i32, align 4
  %value4 = alloca i32, align 4
  %value5 = alloca i32, align 4
  %value6 = alloca i32, align 4
  %value7 = alloca i32, align 4
  %value8 = alloca i32, align 4
  store i32 0, i32* %1
  %2 = call i32 @test35(i32* %value1, i32* %value2, i32* %value3, i32* %value4, i32* %value5, i32* %value6, i32* %value7, i32* %value8)
  ret i32 %2
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
