; ModuleID = '../src/test11.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@memory = internal global i32* @mem1, align 8
@mem1 = internal global i32 291, align 4

; Function Attrs: nounwind
define i32 @test11(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  %2 = load i32* %1, align 4
  %3 = load i32** @memory, align 8
  %4 = load i32* %3, align 4
  %5 = add nsw i32 %2, %4
  store i32 %5, i32* %local, align 4
  %6 = load i32* %local, align 4
  ret i32 %6
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
