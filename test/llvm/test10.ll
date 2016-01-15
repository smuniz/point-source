; ModuleID = '../src/test10.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@mem1 = internal global i32 291, align 4

; Function Attrs: nounwind
define i32 @test10(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  %2 = load i32* %1, align 4
  %3 = load i32* @mem1, align 4
  %4 = add nsw i32 %2, %3
  store i32 %4, i32* %local, align 4
  %5 = load i32* %local, align 4
  ret i32 %5
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
